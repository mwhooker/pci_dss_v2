import os.path

base = os.path.abspath(os.path.dirname(__file__))

outdir = os.path.join(base, 'markout')
indir = os.path.join(base, 'ocrtxt')


def parse(filename):
    sections = []
    section = []
    parsing = False
    with open(filename) as f:
        for line in (l.strip() for l in f):
            if line.lstrip().startswith('6'):
                if parsing:
                    sections.append(section)
                    section = []
                    parsing = False
                    #print "%s<--'" % line
                else:
                    #print "'-->%s" % line
                    section.append(line)
                    parsing = True
            elif parsing:
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

    for fln in parsed.keys():
        print "[generating] %s" % fln
        with open(os.path.join(outdir, "./%s.md" % fln), 'w+') as f2:
            for sections in parsed[fln]:
                secnum = sections[0].split()[0]
                f2.write("## [%s](#%s)\n" % (secnum, secnum))
                f2.write(" ".join(sections))
                f2.write("\n")


os.path.walk(indir, cb, None)
