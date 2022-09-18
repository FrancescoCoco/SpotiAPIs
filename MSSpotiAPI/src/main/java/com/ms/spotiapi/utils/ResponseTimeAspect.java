package com.ms.spotiapi.utils;

import io.micrometer.core.instrument.Gauge;
import io.micrometer.core.instrument.MeterRegistry;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.reflect.MethodSignature;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.lang.annotation.Annotation;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.List;


//It specifies that class is an Aspect Class.
@Aspect
//It specifies that the class is a Spring bean
@Component
public class ResponseTimeAspect {
    private static Logger log = LoggerFactory.getLogger(ResponseTimeAspect.class);

    private List<Long> list_responses_time;

    @Autowired
    MeterRegistry meterRegistry;

    public ResponseTimeAspect(){
        list_responses_time = new ArrayList<>();
    }

    @Around("@annotation(ResponseTimeTracking)")
    public Object responseTime(ProceedingJoinPoint pjp) throws  Throwable{
        Object result = null;
        Method method= ((MethodSignature)pjp.getSignature()).getMethod();
        Annotation[] annotations = method.getDeclaredAnnotations(); method.getDeclaredAnnotations();
        for(Annotation annotation: annotations){
            if (annotation instanceof ResponseTimeTracking){
                ResponseTimeTracking responseTimeTracking = (ResponseTimeTracking) annotation;
                long startTime = System.currentTimeMillis();
                result = pjp.proceed();
                long endTime = System.currentTimeMillis();
                long TimeTaken = endTime-startTime;
                list_responses_time.add(TimeTaken);
                Gauge.builder("response_time_"+method.getName(), list_responses_time, value -> list_responses_time.get(list_responses_time.size()-1))
                        .description("response_time_"+method.getName())
                        .register(meterRegistry);

                logTimeTaken(pjp.getSignature().getDeclaringTypeName()+"-"+ pjp.getSignature().getName(),TimeTaken,responseTimeTracking.unit());
            }
        }
        return result ;
    }

    public static void logTimeTaken(String fqdnMethodName, long timeTaken, TimeUnit timeUnit) {
        log.info("@Timed method={}, time={}, unit={}", fqdnMethodName , timeTaken,timeUnit);
    }


}
