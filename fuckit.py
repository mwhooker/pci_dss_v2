import os.path

base = os.path.abspath(os.path.dirname(__file__))

outdir = os.path.join(base, 'markout')
indir = os.path.join(base, 'ocrtxt')


def parse(filename):
    sections = []
    section = []
    with open(filename) as f:
        for line in (l.strip() for l in f if len(l.strip())):
            if line.startswith('6'):
                if len(section):
                    sections.append(section)
                    section = []
            #print line
            section.append(line)
    if len(section):
        #print "<--'"
        sections.append(section)

    return sections


def cb(arg, dirname, filenames):
    parsed = {}
    for f in filenames:
        parsed[f] = parse(os.path.join(dirname, f))

    ssect = []
    for fname, sections in parsed.items():
        print "[generating] %s" % fname
        for section in sections:
            secnum = section[0].split()[0]
            ssect.append((secnum, section))

    with open(os.path.join(outdir, 'section.md'), 'w+') as outf:
        for secnum, section in sorted(ssect):
            outf.write("## [%s](#%s)\n" % (secnum, secnum))
            outf.write(" ".join(section))
            outf.write("\n")

os.path.walk(indir, cb, None)
