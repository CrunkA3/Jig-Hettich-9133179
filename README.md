# Jig for Hettich 9133179 Hinge Assembly

A parametric CadQuery-based jig design for drilling and aligning the Hettich 9133179 hinge components.

## Overview

This project generates a precision jig for manufacturing and assembly of the Hettich 9133179 hinge system. The jig includes:

- **Base plane** - Provides a stable reference surface
- **Vertical walls** - Holds and positions workpieces
- **Triangular ribs** - Adds structural stability and prevents deflection
- **Hinge slots** - Pre-cut openings sized for the hinge components

## Requirements

- Python 3.8+
- [CadQuery](https://cadquery.readthedocs.io/) - Parametric CAD programming library
- [OCP VSCode](https://github.com/bernhard-42/vscode-ocp-cad-viewer) - Visual debugging for OCP/CadQuery models (optional, for development)

## Installation

```bash
pip install cadquery ocp-vscode
```

## Usage

Run the script to generate the jig model:

```bash
python JIG-Hettich-9133179.py
```

This will:
1. Generate the jig geometry
2. Display the model in OCP VSCode (if running in VS Code with the extension)
3. Export the model to `jig-Hettich-9133179.stl` and `jig-Hettich-9133179.step`

## Model Specifications

### Hinge Dimensions
- **Diameter**: 13.5 mm
- **Length**: 61.5 mm
- **Inner Length**: 31.7 mm
- **Depth**: 6.5 mm
- **Inner Depth**: 18.5 mm
- **Counter Distance**: 46.5 mm

### Board Dimensions
- **Thickness**: 28 mm
- **Width**: 100 mm
- **Length**: 200 mm

### Jig Dimensions
- **Width**: 150 mm
- **Depth**: 150 mm
- **Height**: 100 mm
- **Top Thickness**: Based on bit cut length

## Project Files

- `JIG-Hettich-9133179.py` - Main Python script generating the jig
- `jig-Hettich-9133179.step` - 3D model in STEP format
- `9133179.3mf` - Hinge model in 3MF format
- `9133179_3D.dwg` - Hinge 3D drawing (AutoCAD format)
- `9133179_3D.DXF` - Hinge 3D drawing (DXF format)
- `9133179_2D_front_view.DXF` - Hinge 2D front view (DXF format)

## Customization

Edit the constants at the top of `JIG-Hettich-9133179.py` to modify:

- `BOARD_THICKNESS`, `BOARD_WIDTH`, `BOARD_LENGTH` - Workpiece dimensions
- `HINGE_DIAMETER`, `HINGE_LENGTH` - Hinge opening specifications
- `BIT_CUT_LENGTH` - Tool bit depth

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## References

- [CadQuery Documentation](https://cadquery.readthedocs.io/)
- [Hettich Hardware](https://www.hettich.com/)
