/* 
* @Author: pc-cjkmt-21
* @Date:   2016-02-23 16:11:33
* @Last Modified by:   pc-cjkmt-21
* @Last Modified time: 2016-02-23 16:19:20
*/

public class Student {
    public static void main(String[] args) {
        class OP{
            String name;
            int age;
            float score;
            void say(){
                System.out.println("姓名:" + name + " 年龄:" + age + " 分数:" + score);
            }
        }
        OP O = new OP();
        O.name = "王向波";
        O.age = 30;
        O.score = 95.5f;
        O.say();
    }
}