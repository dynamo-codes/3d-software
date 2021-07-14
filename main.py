import pyglet
import pyglet.gl

pos = [0, 0, -20]
rot_y = 0

config = pyglet.gl.Config(sample_buffers=1, samples=8)
tela = pyglet.window.Window(height=500, width=500, config=config)

@tela.event
def on_draw():

    global pos_z, rot_y

    tela.clear()

    pyglet.gl.glMatrixMode(pyglet.gl.GL_PROJECTION)
    pyglet.gl.glLoadIdentity()
    pyglet.gl.gluPerspective(90, 1, 0.1, 100)

    pyglet.gl.glMatrixMode(pyglet.gl.GL_MODELVIEW)
    pyglet.gl.glLoadIdentity()

    pyglet.gl.glTranslatef(*pos)
    pyglet.gl.glRotatef(rot_y, 0, 1, 0)

    pyglet.gl.glBegin(pyglet.gl.GL_POLYGON)
    pyglet.gl.glVertex3f(-5,-5,0)
    pyglet.gl.glVertex3f(5,-5,0)
    pyglet.gl.glVertex3f(0,5,0)
    pyglet.gl.glEnd()

    pyglet.gl.glFlush()
@tela.event
def on_key_press(s,m):

    global pos_z, rot_y
    """
    if s == pyglet.window.key.W:
        pos[2] -= 3
    if s == pyglet.window.key.S:
        pos[2] += 3
    """
    if s == pyglet.window.key.W:
        pos[1] += 3
    if s == pyglet.window.key.S:
        pos[1] -= 3
    if s == pyglet.window.key.A:
        pos[0] -= 3
    if s == pyglet.window.key.D:
        pos[0] += 3
    """
    if s == pyglet.window.key.A:
        rot_y += 10
    if s == pyglet.window.key.D:
        rot_y -= 10
    """

pyglet.app.run()
