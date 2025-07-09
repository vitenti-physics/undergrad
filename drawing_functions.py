"""Functions for drawing the Euclidean plane in 2D with orthonormal basis vectors."""

import matplotlib as mpl

# Constants
CP_LEN = 1.5
HEAD_WIDTH = 0.03
LW_DASH = 1
ARROWPROPS = dict(arrowstyle="->", linewidth=2)


def draw_euclidean_2d(ax: mpl.axes.Axes, title: str | None = None) -> None:
    """Draws the Euclidean plane in 2D with orthonormal basis vectors."""
    # Axes
    if title is not None:
        ax.set_title(title)

    ax.annotate("", xy=(CP_LEN, 0), xytext=(0, 0), arrowprops=ARROWPROPS)
    ax.annotate("", xy=(0, CP_LEN), xytext=(0, 0), arrowprops=ARROWPROPS)
    ax.text(CP_LEN + 0.05, 0, r"$\vec{e}^1$", fontsize=14, verticalalignment="center")
    ax.text(0.0, CP_LEN + 0.05, r"$\vec{e}^2$", fontsize=14, horizontalalignment="left")

    # Layout
    ax.set_xlim(-0.2, CP_LEN + 0.2)
    ax.set_ylim(-0.2, CP_LEN + 0.2)
    ax.set_aspect("equal")
    ax.axis("off")


def draw_vector_2d(
    ax: mpl.axes.Axes,
    vector: tuple[float, float],
    *,
    label: str | None = None,
    components: bool = False,
    color: str = "black",
    label_offset: tuple[float, float] = (0.02, 0.02),
    **kwargs,
) -> None:
    """Draws a vector from the origin in 2D Euclidean space using quiver."""
    x, y = vector
    ax.quiver(0, 0, x, y, angles="xy", scale_units="xy", scale=1, color=color, **kwargs)

    if label is not None:
        ax.text(
            x + label_offset[0],
            y + label_offset[1],
            rf"$\vec{{{label}}}$",
            fontsize=14,
            color=color,
        )

    if components:
        # First component (x-direction)
        ax.quiver(
            0, 0, x, 0, angles="xy", scale_units="xy", scale=1, color="gray", alpha=0.6
        )
        ax.plot([0.0, x], [y, y], color="black", linestyle="--", linewidth=LW_DASH)
        ax.text(x + 0.01, 0.0, rf"${label}^1$", fontsize=14, color=color)

        # Second component (y-direction)
        ax.quiver(
            0, 0, 0, y, angles="xy", scale_units="xy", scale=1, color="gray", alpha=0.6
        )
        ax.plot([x, x], [0.0, y], color="black", linestyle="--", linewidth=LW_DASH)
        ax.text(0.0, y + 0.01, rf"${label}^2$", fontsize=14, color=color)
