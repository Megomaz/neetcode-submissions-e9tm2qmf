class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        print(path)
        paths = []

        for p in path:
            if p == '/' or p == '.' or p == "":
                continue
            if p == '..':
                if paths:
                    paths.pop()
            else:
                paths.append(p)
        print(paths)
        return '/' + '/'.join(paths)
        
