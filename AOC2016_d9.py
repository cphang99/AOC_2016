import re
import string

#pt1
def c1():
    with open('d9input.txt', 'r') as f:
        m_regex = r'\(([0-9]+)x([0-9]+)\)'
        regexp = re.compile(m_regex)
        for content in f:
            newcontent = content
            ignoreMarker = -1
            prev_end = 0
            num_sections = 0
            for m in re.finditer(m_regex, content):
                if ignoreMarker > m.end(): continue
                num_sections += 1
                marker = content[m.start():m.end()]
                if prev_end != m.start():
                    num_sections += 1

                chunk_i = int(content[m.start(1):m.end(1)])
                chunk = content[m.end():m.end()+chunk_i]
                ignoreMarker = m.end() + chunk_i
                prev_end = ignoreMarker
                numReps = int(content[m.start(2):m.end(2)])
                s = str()
                for i in xrange(numReps):
                    s = s + chunk
                newcontent = newcontent.replace(marker + chunk, s, 1)
            newcontent = newcontent.translate(None, string.whitespace)
            print(len(newcontent))

#pt2 
def c2():
    with open('d9input.txt', 'r') as f:
        for content in f:
            print(main_sec(content))

def d_complete(content):
        m_regex = r'\(([0-9]+)x([0-9]+)\)'
        regexp = re.compile(m_regex)
        newcontent = content
        #Continue until there are no more markers
        while(regexp.search(newcontent) is not None):
            ignoreMarker = -1
            content = newcontent
            #On each pass, find all markers and decompress
            #As in pt1, we continue reading the file after the repeated data
            #So on each pass we are likely to have leftover markers
            for m in re.finditer(m_regex, content):
                if ignoreMarker > m.end(): continue
                marker = content[m.start():m.end()]
                chunk_i = int(content[m.start(1):m.end(1)])
                chunk = content[m.end():m.end()+chunk_i]
                ignoreMarker = m.end() + chunk_i
                numReps = int(content[m.start(2):m.end(2)])
                s = str()
                for i in xrange(numReps):
                    s = s + chunk
                newcontent = newcontent.replace(marker + chunk, s, 1)
        newcontent = newcontent.translate(None, string.whitespace)
        return len(newcontent)

def main_sec(content):
    m_regex = r'\(([0-9]+)x([0-9]+)\)'
    regexp = re.compile(m_regex)
    newcontent = content
    ignoreMarker = -1
    prev_end = 0
    sections = []
    num_sections = 0
    #Break into sections as defined in pt1
    for m in re.finditer(m_regex, content):
        if ignoreMarker > m.end(): continue
        num_sections += 1
        marker = content[m.start():m.end()]
        if prev_end != m.start():
            num_sections += 1
            sections.append(content[prev_end:m.start()])

        chunk_i = int(content[m.start(1):m.end(1)])
        chunk = content[m.end():m.end()+chunk_i]
        ignoreMarker = m.end() + chunk_i
        prev_end = ignoreMarker
        numReps = int(content[m.start(2):m.end(2)])
        sections.append(marker+chunk)
    if len(content)-1 > prev_end:
        num_sections += 1
        sections.append(content[prev_end:].translate(None,
            string.whitespace))

    #Evaluate each section, in exp, this should be as small as possible
    #to obtain a result i.e. evaluation is much more expensive than
    #recursion. d_complete() actually calculates the decompressed size
    tot = 0
    for s in sections:
        if re.match(m_regex, s) and int(re.match(m_regex, s).group(1)) > 5:
            end = re.match(m_regex,s).end()
            mult = re.match(m_regex,s).group(2)
            tot += int(mult) * main_sec(s[end:])
        else:
            tot += d_complete(s)
    return tot

c1()
c2()
