// Online C compiler to run C program online
#include <stdio.h>

int main() 
{
    int arr[]={5,4,93,9,7,2,1};
    int temp;
    for(int i=0;i<7;i++)
    {
        for(int j=0;j<7;j++)
        {
            if(arr[j+1] <arr[j])
            {
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
    for(int i=0;i<7;i++)
    {
        printf("%d ",arr[i]);
    }
    return 0;
}