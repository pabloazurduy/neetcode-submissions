class Solution:

    def encode(self, strs: List[str]) -> str:
        return repr(strs)

    def decode(self, s: str) -> List[str]:
        return eval(s)