def solution(ip_addrs, langs, scores):
    N = len(ip_addrs)

    same_ip = dict()
    for i in range(N) :
        if ip_addrs[i] not in same_ip :
            same_ip[ip_addrs[i]] = []
        same_ip[ip_addrs[i]].append(i)
        # 언어도 변경
        if langs[i] == "C++" or langs[i] == "C#" :
            langs[i] = "C"

    answer = N
    for ip in same_ip.keys() :
        if len(same_ip[ip]) >= 4 :
            answer -= len(same_ip[ip])
        elif len(same_ip[ip]) == 3 :
            if langs[same_ip[ip][0]] == langs[same_ip[ip][1]] and langs[same_ip[ip][1]] == langs[same_ip[ip][2]] :
                answer -= 3
        elif len(same_ip[ip]) == 2 :
            if langs[same_ip[ip][0]] == langs[same_ip[ip][1]] and scores[same_ip[ip][0]] == scores[same_ip[ip][1]] :
                answer -= 2
    return answer

print(solution(["5.5.5.5", "155.123.124.111", "10.16.125.0", "155.123.124.111", "5.5.5.5", "155.123.124.111", "10.16.125.0", "10.16.125.0"], ["Java", "C++", "Python3", "C#", "Java", "C", "Python3", "JavaScript"], [294, 197, 373, 45, 294, 62, 373, 373]))