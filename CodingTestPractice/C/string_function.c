// https://csacademy.com/workspace
#include <string.h>
#include <stdio.h>

char str[100] = "hello";

void insert(int index, char value){
    // 해당 index 뒤로 한칸씩 밀어서 복사
    memmove(str+index+1, str+index, strlen(str)-index+1);
    str[index] = value;
}

char pop(int index){
    char value = str[index];
    memmove(str+index, str+index+1, strlen(str)-index);
    return value;
}

void append(char value){
    insert(strlen(str), value);
}

void copy(char *str1, char *str2){
    memcpy(str2, str1, strlen(str1)+1);
}

int is_equal(char *str1, char *str2){
    if(memcmp(str1, str2, strlen(str1)) == 0) return 1;
    return 0;
}

void main() {
    insert(3, '!');
    printf("%s \n", str);  // hel!lo 
    printf("%c - %s \n", pop(3), str); // ! - hello 
    append('!');
    printf("%s \n", str);  // hello! 

    char str2[100];
    printf("%s \n", str2);  // 
    copy(str, str2);
    printf("%s \n", str2);  // hello! 
    printf("%d \n", is_equal(str, str2)); // 1

    str2[1] = '5';
    printf("%s \n", str);   // hello! 
    printf("%s \n", str2);  // h5llo! 
    printf("%d", is_equal(str, str2)); //0

    // int를 char로 저장하기
    char value[100];
    sprintf(value, "%d", 8);
    printf("%s \n", value); // 8 - 이때 자료형은 string
    append(value[0]);
    printf("%s \n", str);   // hello!8

}