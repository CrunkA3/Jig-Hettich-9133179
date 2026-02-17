"""
Jig design for Hettich 9133179 hinge assembly.

This module generates a CadQuery-based jig for drilling and aligning the Hettich 9133179
hinge components. It creates a base structure with stability ribs and defines methods for
hole creation and positioning.
"""

from cadquery import cq, exporters, importers

from ocp_vscode import show_object, show


BOARD_THICKNESS = 28
BOARD_WIDTH = 100
BOARD_LENGTH = 200

HINGE_DIAMETER = 13.5
HINGE_LENGTH = 61.5
HINGE_LENGTH_INNER = 31.7
HINGE_COUNTER_DISTANCE = 46.5

HINGE_DEPTH = 6.5
HINGE_DEPTH_INNER = 18.5

BIT_CUT_LENGTH = 25.4


board = (
    cq.Workplane("XZ")
    .box(BOARD_LENGTH, BOARD_WIDTH, BOARD_THICKNESS, centered=(True, False, True))
    .translate((0, 0, -BOARD_WIDTH))
)


def jig():
    """Create a jig for the Hettich 9133179 hinge.
    
    Returns:
        A CadQuery workplane object representing the complete jig assembly,
        including the base plane, walls, triangular ribs for stability,
        and with the board removed from the structure.
    """
    # dimensions in mm
    jig_plane_depth = 150
    jig_plane_thickness = 10

    width = 150
    height = 100
    thickness = BOARD_THICKNESS + 10  # add some extra thickness for wall

    # top thickness of the jig
    top_thickness = BIT_CUT_LENGTH - HINGE_DEPTH + 10  # add some extra thickness

    # create the base of the jig
    jig_base = (
        cq.Workplane("XY")
        .rect(width, jig_plane_depth)
        .extrude(-jig_plane_thickness)
        .edges("|Z")
        .fillet(25)
        .faces("<Z")
        .rect(width, thickness)
        .extrude(-height)
        .translate((0, 0, top_thickness))
    )

    # triangular ribs between base plane and wall for stability
    rib_width = jig_plane_depth * 0.75
    rib_depth = 10
    rib_height = rib_width * 0.75
    rib_x_offset = (width / 2) - (rib_width / 2)

    rib = (
        cq.Workplane("YZ")
        .polyline([(-rib_width / 2, 0), (rib_width / 2, 0), (0, -rib_height)])
        .close()
        .extrude(-rib_depth)
    )

    jig_base = jig_base.union(rib.translate((rib_x_offset, 0, top_thickness)))
    jig_base = jig_base.union(rib.translate((-rib_x_offset, 0, top_thickness)))
    jig_base = jig_base - board

    return jig_base


def hinge_top(self):
    """Create the top hole for the hinge.
    
    Args:
        self: The CadQuery workplane object.
        
    Returns:
        The modified workplane with a through-slot cut for the hinge opening,
        sized to HINGE_LENGTH by HINGE_DIAMETER.
    """
    result = self.slot2D(HINGE_LENGTH, HINGE_DIAMETER, 0).cutThruAll()
    return result


cq.Workplane.hinge_top = hinge_top


if __name__ == "__main__":
    jig_model = jig()

    jig_model = jig_model.faces(">Z").workplane().hinge_top()

    show_object(jig_model)
    # show_object(board, transparent=0.5)

    # export the model to a file
    exporters.export(jig_model, "jig-Hettich-9133179.stl")
    exporters.export(jig_model, "jig-Hettich-9133179.step")
