import sys
from solid import *
from solid.objects import *
from solid.utils import *

SEGMENTS = 100
rad =10
Rad =50
N=10

def inner():
	res=color([0.6,0.7,1])(
		rotate_extrude(convexity = 10)(
			difference()(
				translate([Rad-rad, 0, 0])(square(size=[rad,2.5*rad], center=True)),
				translate([Rad, 0, 0])(circle(r=rad))
		)))
	return res

def outer():
	res=color([0.6,1,0.4])(
		rotate_extrude(convexity = 10)(
			difference()(
				translate([Rad+rad, 0, 0])(square(size=[rad,2.5*rad], center=True)),
				translate([Rad, 0, 0])(circle(r=rad))
		)))
	return res


def balls():
	res=sphere(0)
	for i in range(N):
		res += rotate(i*360/N, [0,0,1])(translate([0,Rad,0])(color("red")(sphere(rad))))
	return res


if __name__ == '__main__':
	out_dir = sys.argv[1] if len(sys.argv) > 1 else None
	
	a = inner()+balls()+outer()

	file_out = scad_render_to_file(a, out_dir=out_dir, file_header=f'$fn = {SEGMENTS};', include_orig_code=True)
	print(f"{__file__}: SCAD file written to: \n{file_out}")



