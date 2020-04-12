from pymol import cmd


@cmd.extend
def _cartoon(selection='all'):
    """
    Draw `selection` in a cartoon style.

    """

    cmd.show('spheres', selection)
    cmd.set('sphere_scale', 0.23, selection)

    cmd.hide('sticks', selection)
    cmd.show('lines', selection)
    cmd.set('line_as_cylinders', 1)
    cmd.set('line_radius', 0.08)
    cmd.set('line_use_shader', 1)
    cmd.set('valence_mode', 0, selection)
    cmd.set('valence_size', 0.14, selection)

    cmd.set('ray_trace_mode', 3)
    cmd.set('ray_trace_color', 'black')

    cmd.set_color('lgray', [0.6, 0.6, 0.6])
    cmd.color('lgray', 'elem C')

    cmd.orient(selection)
    cmd.zoom(selection, 3, complete=1)


cmd.auto_arg[0]['_cartoon'] = [
    cmd.object_sc,
    'the selection, which is to be turned into a cartoon style',
    ',',
]
