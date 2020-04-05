def solution(directory, command):

    for c in command :
        cmd = c.split()
        if cmd[0] == "mkdir" :
            directory.append(cmd[1])
        elif cmd[0] == "rm" :
            target = []
            for l in range(len(directory)) :
                if cmd[1] in directory[l][:len(cmd[1])] :
                    target.append(l)
            target.sort(reverse=True)
            for l in target :
                directory.pop(l)
        elif cmd[0] == "cp" : 
            target = []
            for l in range(len(directory)) :
                if cmd[1] in directory[l][:len(cmd[1])] :
                    target.append(directory[l])
            for t in target :
                directory.append(cmd[2]+t)
        
    return sorted(directory)



print(solution([
"/",
"/hello",
"/hello/tmp",
"/root",
"/root/abcd",
"/root/abcd/etc",
"/root/abcd/hello"
],[
"mkdir /root/tmp",
"cp /hello /root/tmp", 
"rm /hello"
]))



"""
[
"/", 
"/root", 
"/root/abcd", 
"/root/abcd/etc", 
"/root/abcd/hello", 
"/root/tmp", 
"/root/tmp/hello", 
"/root/tmp/hello/tmp"
]
"""

""" 
그래프로도 풀어보자
"""