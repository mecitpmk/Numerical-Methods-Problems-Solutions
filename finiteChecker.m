function finiteChecker(startFrom,endFrom)
    incrementType = 0;
    if (startFrom > endFrom)
        incrementType = -1;
    else
        incrementType = 1;
    end
    
    s=0;
    for i=startFrom:incrementType:endFrom
        s=s+1/i^4;
    end
    fprintf('Value is : %.20f \n',s);
    errorCalculation = ((pi^4)/90 -s)/((pi^4)/90);
    fprintf('Error :');
    disp(errorCalculation);

end