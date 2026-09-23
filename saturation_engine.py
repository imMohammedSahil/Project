"""
Research Scope AI - Saturation Engine & Visual Matrix
Calculates evidence-based research saturation metrics and generates interactive Plotly charts.
"""
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Tuple
import plotly.graph_objects as go
from academic_retrieval import Paper

@dataclass
class SaturationMetrics:
    cluster_name: str
    saturation_score: float  # 0.0 to 1.0
    saturation_level: str    # "Low", "Moderate", "High", "Critical"
    scope_potential: float   # 0.0 to 1.0
    paper_count: int
    recent_activity_ratio: float  # % of papers >= 2023
    avg_citations: float
    saturation_rationale: str
    yearly_distribution: Dict[int, int] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class SaturationEngine:
    """Calculates multi-signal literature saturation and plots 2D Landscape & Timeline charts."""

    def compute_cluster_saturation(
        self,
        cluster_name: str,
        papers: List[Paper],
        similarity_to_user: float
    ) -> SaturationMetrics:
        """Computes multi-signal evidence-based saturation index for a research cluster."""
        count = len(papers)
        if count == 0:
            return SaturationMetrics(
                cluster_name=cluster_name,
                saturation_score=0.20,
                saturation_level="Low",
                scope_potential=0.85,
                paper_count=0,
                recent_activity_ratio=0.0,
                avg_citations=0.0,
                saturation_rationale="Sparse literature detected. High opportunity for foundational contributions."
            )

        # 1. Year distribution & Velocity
        years = [p.year for p in papers if p.year and 2018 <= p.year <= 2026]
        recent_years = [y for y in years if y >= 2023]
        recent_ratio = len(recent_years) / len(years) if years else 0.5

        yearly_counts = {yr: years.count(yr) for yr in range(2019, 2027)}

        # 2. Citation concentration
        citations = [p.citation_count for p in papers]
        avg_cit = sum(citations) / count if count > 0 else 0.0

        # 3. Saturation formula (Weighted composite)
        # S = 0.40*(volume_norm) + 0.45*(citation_density) + 0.15*(historical_maturity)
        vol_norm = min(1.0, count / 10.0)
        cit_norm = min(1.0, avg_cit / 150.0)
        historical_maturity = 1.0 - (recent_ratio * 0.5)  # Older literature has higher baseline maturity

        raw_saturation = (0.35 * vol_norm) + (0.45 * cit_norm) + (0.20 * historical_maturity)
        saturation_score = max(0.10, min(0.98, round(raw_saturation, 2)))

        if saturation_score >= 0.65:
            level = "High Saturation"
            rationale = f"Heavily investigated area with high citation density (avg {avg_cit:.0f} cites) and established benchmark models."
        elif saturation_score >= 0.35:
            level = "Moderate Saturation"
            rationale = f"Active research direction with steady publication velocity ({recent_ratio*100:.0f}% recent papers since 2023)."
        else:
            level = "Low Saturation (Emerging)"
            rationale = "Sparse prior art with few dedicated multimodal studies. High potential for novel architectural design."

        # Scope potential = high user relevance + space for novel contribution (1 - 0.4*saturation)
        scope_potential = round(min(0.98, max(0.15, (similarity_to_user * 0.65) + ((1.0 - saturation_score) * 0.35))), 2)

        return SaturationMetrics(
            cluster_name=cluster_name,
            saturation_score=saturation_score,
            saturation_level=level,
            scope_potential=scope_potential,
            paper_count=count,
            recent_activity_ratio=round(recent_ratio, 2),
            avg_citations=round(avg_cit, 1),
            saturation_rationale=rationale,
            yearly_distribution=yearly_counts
        )

    def generate_saturation_matrix_plot(self, metrics_list: List[SaturationMetrics]) -> go.Figure:
        """Generates interactive Plotly 2D Scatter Matrix: Scope Potential vs Saturation."""
        fig = go.Figure()

        # Add quadrant background annotations & shapes
        fig.add_shape(type="rect", x0=0.0, y0=0.5, x1=0.5, y1=1.0, fillcolor="rgba(239, 68, 68, 0.07)", line_width=0, layer="below")
        fig.add_shape(type="rect", x0=0.5, y0=0.5, x1=1.0, y1=1.0, fillcolor="rgba(234, 179, 8, 0.07)", line_width=0, layer="below")
        fig.add_shape(type="rect", x0=0.5, y0=0.0, x1=1.0, y1=0.5, fillcolor="rgba(16, 185, 129, 0.12)", line_width=0, layer="below")
        fig.add_shape(type="rect", x0=0.0, y0=0.0, x1=0.5, y1=0.5, fillcolor="rgba(99, 102, 241, 0.07)", line_width=0, layer="below")

        # Add quadrant labels
        fig.add_annotation(x=0.25, y=0.92, text="<b>Saturated Baseline</b><br><span style='font-size:10px;color:#94a3b8'>Crowded / Incremental Gaps</span>", showarrow=False, font=dict(color="#F87171", size=11))
        fig.add_annotation(x=0.75, y=0.92, text="<b>Competitive High-Impact</b><br><span style='font-size:10px;color:#94a3b8'>High Interest / High Activity</span>", showarrow=False, font=dict(color="#FBBF24", size=11))
        fig.add_annotation(x=0.75, y=0.08, text="<b>OPTIMAL SCOPE (HIGH OPPORTUNITY)</b><br><span style='font-size:10px;color:#94a3b8'>High Relevance / Uncrowded Space</span>", showarrow=False, font=dict(color="#34D399", size=12))
        fig.add_annotation(x=0.25, y=0.08, text="<b>Emerging Niche</b><br><span style='font-size:10px;color:#94a3b8'>Sparse / Foundational Exploration</span>", showarrow=False, font=dict(color="#818CF8", size=11))

        # Plot cluster points
        x_vals = [m.scope_potential for m in metrics_list]
        y_vals = [m.saturation_score for m in metrics_list]
        labels = [m.cluster_name for m in metrics_list]
        hover_texts = [
            f"<b>{m.cluster_name}</b><br>"
            f"Scope Potential: <b>{m.scope_potential:.2f}</b><br>"
            f"Saturation Index: <b>{m.saturation_score:.2f}</b> ({m.saturation_level})<br>"
            f"Papers Analyzed: {m.paper_count}<br>"
            f"Avg Citations: {m.avg_citations}<br>"
            f"<i>{m.saturation_rationale}</i>"
            for m in metrics_list
        ]

        fig.add_trace(go.Scatter(
            x=x_vals,
            y=y_vals,
            mode="markers+text",
            marker=dict(
                size=[max(18, min(36, m.paper_count * 5)) for m in metrics_list],
                color=y_vals,
                colorscale="Viridis",
                showscale=True,
                colorbar=dict(title="Saturation", thickness=12, len=0.7, tickfont=dict(color="#CBD5E1")),
                line=dict(color="#FFFFFF", width=2)
            ),
            text=labels,
            textposition="top center",
            textfont=dict(color="#F1F5F9", size=12, family="Inter, sans-serif"),
            hoverinfo="text",
            hovertext=hover_texts
        ))

        # Crosshair lines at 0.5
        fig.add_hline(y=0.5, line_dash="dash", line_color="rgba(148, 163, 184, 0.4)", line_width=1)
        fig.add_vline(x=0.5, line_dash="dash", line_color="rgba(148, 163, 184, 0.4)", line_width=1)

        fig.update_layout(
            title="<b>Research Landscape: Scope Potential × Research Saturation</b>",
            title_font=dict(color="#F8FAFC", size=16),
            xaxis=dict(
                title="<b>Scope Potential (Novelty & Feasibility)</b>",
                title_font=dict(color="#CBD5E1"),
                range=[-0.02, 1.05],
                gridcolor="rgba(51, 65, 85, 0.3)",
                tickfont=dict(color="#94A3B8")
            ),
            yaxis=dict(
                title="<b>Research Saturation Index (Literature Volume & Citations)</b>",
                title_font=dict(color="#CBD5E1"),
                range=[-0.02, 1.05],
                gridcolor="rgba(51, 65, 85, 0.3)",
                tickfont=dict(color="#94A3B8")
            ),
            template="plotly_dark",
            paper_bgcolor="#0B0F19",
            plot_bgcolor="#0F172A",
            margin=dict(l=60, r=40, t=60, b=60),
            height=460
        )
        return fig

    def generate_timeline_plot(self, metrics_list: List[SaturationMetrics]) -> go.Figure:
        """Generates publication timeline velocity chart across years (2019-2026)."""
        fig = go.Figure()
        years = list(range(2019, 2027))

        colors = ["#6366F1", "#06B6D4", "#10B981", "#F59E0B", "#EC4899", "#8B5CF6"]

        for idx, m in enumerate(metrics_list):
            y_counts = [m.yearly_distribution.get(yr, 0) for yr in years]
            fig.add_trace(go.Scatter(
                x=years,
                y=y_counts,
                mode="lines+markers",
                name=m.cluster_name,
                line=dict(color=colors[idx % len(colors)], width=3),
                marker=dict(size=7)
            ))

        fig.update_layout(
            title="<b>Publication Activity & Growth Velocity (2019 – 2026)</b>",
            title_font=dict(color="#F8FAFC", size=15),
            xaxis=dict(
                title="Publication Year",
                tickmode="linear",
                tick0=2019,
                dtick=1,
                gridcolor="rgba(51, 65, 85, 0.3)",
                tickfont=dict(color="#94A3B8")
            ),
            yaxis=dict(
                title="Number of Published Papers",
                gridcolor="rgba(51, 65, 85, 0.3)",
                tickfont=dict(color="#94A3B8")
            ),
            template="plotly_dark",
            paper_bgcolor="#0B0F19",
            plot_bgcolor="#0F172A",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(color="#CBD5E1")),
            margin=dict(l=50, r=30, t=60, b=50),
            height=340
        )
        return fig

# Global saturation engine instance
saturation_engine = SaturationEngine()
