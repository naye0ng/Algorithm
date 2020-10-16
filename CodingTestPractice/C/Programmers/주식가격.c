#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

struct Node{
    int price, time;
};

int* solution(int prices[], size_t prices_len) {
    int* answer = (int*)malloc(sizeof(int)*prices_len);
    struct Node *stack;
    stack = (struct Node*)malloc(sizeof(struct Node)*prices_len);

    int top = 0;
    stack[top].price = prices[0];
    stack[top].time = 0;
    
    int t = 1, price, time;
    while(t < prices_len){
        price = prices[t];
        while(top >=0 && price < stack[top].price){
            time = stack[top].time;
            answer[time] = t-time;
            top--;
        }
        top++;
        stack[top].price = prices[t];
        stack[top].time = t;
        t++;
    }
    
    t--;
    while(top >= 0){
        time = stack[top].time;
        answer[time] = t-time;
        top--;
    }
    
    return answer;
}