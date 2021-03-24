function twoApproaches(x,trueValue)
    
    term1=1;
    term2=1;
    sum1o=term1;
    sum2o=term2;
    
    for i=2: 20
        sum1=sum1o+(-1)^(i-1)*x^(i-1)/factorial(i-1);
        term2=term2+x^(i-1)/factorial(i-1);
        sum2=1/term2;
        et1=abs((trueValue-sum1)/sum1);
        et2=abs((trueValue-sum2)/sum2);
        ea1=abs((sum1-sum1o)/sum1);
        ea2=abs((sum2-sum2o)/sum2);
        sum1o=sum1;
        sum2o=sum2;
    end
    
    my_list = [sum1,et1,ea1,sum2,et2,ea2];
    fthEquation = 'First';
    scthEquation = 'Second';
    currentEquation = fthEquation;
    for i=1:3:length(my_list)
        if (i<4)
            currentEquation = fthEquation;
        else
            currentEquation = scthEquation;
        end
         fprintf('Summation for %s Eq : %s \n',currentEquation,num2str(my_list(i)));
         fprintf('Et for %s Eq: %s \n',currentEquation,num2str(my_list(i+1)));
         fprintf('Error Approx. for %s Eq %s \n\n',currentEquation,num2str(my_list(i+2)));
    end

end