 #include <stdio.h>
 #define MAX_COUNT 5

 typedef struct People
 {
  char name[14];
  unsigned short int age;
  float height;
  float weight;
 } Person;

 int AddFriend
 (Person *p_friend, int count)
 {
  if(count<MAX_COUNT) {
    p_friend = p_friend + count;
    printf("\ninput data");
    printf("1. name")
    scanf("%s" , p_friend -> name);
    printf("2. age:");
    scanf("%hu", &p_friend -> age);
    printf("3. height :");
    scanf("%f", &p_friend -> weight);
    printf("4. weight : ");
    scanf("%f", &p_friend -> weight);
    return 1; /* succeess */

  }else {
    printf("maximum number is 5 \n");
    printf(" you can add %d at maximum \n\n", MAX_COUNT);
  }
  return 0;
 }
 void ShowFriendList(Person *p_friend, int count)
 {
  int i;
  if(count > 0) {
    printf("\n registered friend list\n");
    printf("==========================\n");
    for(i = 0; i < count; i++) {
      printf("%-14s, %3d, %6.2f, %6.2f\n", p_friend -> name, p_friend -> age, p_friend -> height, p_friend -> weight);
      p_friend++; // next friend's address
    }
    printf("=============================\n")
  } else {
    printf("\n no friend in list\n\n");
    )
  }
}

void main()
{
  Person friends[MAX_COUNT];
  int count = 0, num;

  while(1) {
    printf(" [ menu ] \n")
    printf("===============\n");
    printf("1. add friend\n");
    printf("2. view friend list\n");
    printf("3 exit");
    printf("=================\n");
    printf("select number");
    scanf("%d", &num);
    if(num==1){
      if(1==AddFriend(friends, count)) count++;
    }else if(num ==2) {
      ShowFriendList(friends,count);

    }else if(num==3) {
      break;
    } else {
      print(" you can only choice from 1 to 3")
    }
  }
}