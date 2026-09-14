def clip_fa(text: str, max_len: 'int > 0' = 80) -> str:

    end = None
    if len(text) < max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
        
    if end is None:
        end = len(text)
    return text[:end].rstrip()

print(clip_fa.__annotations__)

from inspect import signature

sig2 = signature(clip_fa)
print(sig2.return_annotation)

for param in sig2.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note, ":", param.name, "=", param.default)