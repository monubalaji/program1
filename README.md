# program1
Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
    Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
    Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string
    import java.io.*;
    import java.lang.*;
    import java.lang.Math;
    import java.util.Scanner;
    public class BasicCalculator
    {
    public static void main(String[] args)
    [
    double num1,num2;
    Scanner sc =new Scanner(System.in);
    System.out.println("enter the numbers");
    num1=sc.nextDouble();
    num2=sc.nextDouble();
    System.out.println("enter the operator(+,-,*,/)");
    char op=sc.next().charAt(0);
    double o=0;
    switch(op)
    {
    case1:'+';
      o=num1+num2;
      break;
    case2:'-';
    o=num1-num2;
    break;
    case3:'*';
    o=num1*num2;
    break;
    case4:'/';
    o=num1/num2;
    break;
    }
    default;
    System.out.println("you have been entered wrong input");
    break;
    }
    System.out.println("the final results:");
    System.out.println();
    System.out.println(num1 + " " + op + " " num2 + " = " + 0);
    }
    }
