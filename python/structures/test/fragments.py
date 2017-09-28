# The fragments involved


fragment_file = open('frags.txt')
more_fragments = True

def get_next_fragment():
    '''
    Invariant:  more_fragments = True/False according to "there is at least one line in frags.txt"
    Precondition: If more_fragments is True, each line of frags.txt consists of a (text) fragment 
        ending in a non-blank character
    Postcondition: old(more_fragments) = False AND return = "NO MORE FRAGMENTS"
    -OR- old(more_fragments) = True AND return = the unread line (without newline)
    '''
    global more_fragments

    # First part of Postcondition
    if not more_fragments:
        return "NO MORE FRAGMENTS"

    #Second part of postcondition (more_fragments)
    new_fragment = fragment_file.readline()
    if new_fragment[-1:] == '\n':  # not last line
        return new_fragment[:-1]  # omit newline
    else:  # last line
        more_fragments = False  # for invariant
        return new_fragment  # (no newline present)