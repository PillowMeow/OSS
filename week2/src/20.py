def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))

    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)

    else:
        return '<%s%s />' % (name, attr_str)

from inspect import signature

sig = signature(tag)
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src':'sunset.jpg', 'cls':'framed'}

print(my_tag)

print(bound_args := sig.bind(**my_tag))

for name, value in bound_args.arguments.items():
    print(name, "=", value)

del my_tag['name']

print(bound_args := sig.bind(**my_tag))