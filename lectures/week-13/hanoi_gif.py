import sys, hanoi, getopt
import moviepy.editor as mpy

def make_clip(n, fps) :
    hanoi_states = hanoi.solution_states(n)
    hanoi_frames = [ hanoi.frame(n, s) for s in hanoi_states ]
    clip = mpy.ImageSequenceClip(hanoi_frames, fps = fps)
    return clip

def print_usage() :
    print("Usage: python hanoi_gif.pu [-v,--verbose]"
          "[-d,--disks <num_disks>] [--fps <fps>] output_file")

if __name__ == '__main__' :
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   'vd:',['verbose','disks=','fps='])
    except getopt.GetoptError as err:
        print(err)
        print_usage()
        sys.exit(2)

    if len(args) != 1:
        print_usage()
        sys.exit(2)
    clip_name = args[0]

    verbose = False
    fps = 2
    n = 3
    for opt, val in opts:
        if opt in ('-v', '--verbose'):
            verbose = True
        if opt in ('-d', '--disks'):
            n = int(val)
        if opt in ('--fps'):
            fps = int(val)

    if verbose : print("Generating clip")
    clip = make_clip(n, fps)
    if verbose : print("Clip created. Writing to file {}.".format(clip_name))
    clip.write_gif(clip_name)
    if verbose : print("Done.")
