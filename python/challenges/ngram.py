import sys

long_text = "Mary had a little lamb its fleece was white as snow; " \
            "And everywhere that Mary went, the lamb was sure to go. " \
            "It followed her to school one day, which was against the rule; " \
            "It made the children laugh and play, to see a lamb at school. " \
            "And so the teacher turned it out, but still it lingered near, " \
            "And waited patiently about till Mary did appear." \
            "\"Why does the lamb love Mary so?\" the eager children cry;\" " \
            "\"Why, Mary loves the lamb, you know\" the teacher did reply.\" "
long_text = long_text.replace(",", "").replace(".", "").replace(";", "")
text_list = long_text.split(" ")


def ngrams(word, n):
    output = {}
    total = 0;
    for i in range(len(text_list) - n):
        g = ' '.join(text_list[i:i + n])
        if g.startswith(word):
            total += 1
            output.setdefault(g, 0)
            output[g] += 1

    d = {k.replace(word + " ", ""): v / total for k, v in output.items() if True}

    return {v[0]: v[1] for v in sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))}


print(ngrams("the", 2))
