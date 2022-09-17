package com.ms.spotiapi.utils;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

//It specifies where the annotation should be applied.
// Because it is at the method level in our case,
// we pass ElementType.METHOD as a parameter
@Target(ElementType.METHOD)
//It specifies when to use this annotation, which in our case is at run time.
@Retention(RetentionPolicy.RUNTIME)
public @interface ResponseTimeTracking {

        /**
         * TimeUnit is unit of time in which you want to log time.
         */
        TimeUnit unit() default TimeUnit.MILLI;

}
