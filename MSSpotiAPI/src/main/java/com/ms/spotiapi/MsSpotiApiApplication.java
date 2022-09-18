package com.ms.spotiapi;

import io.micrometer.core.aop.TimedAspect;
import io.micrometer.core.instrument.MeterRegistry;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@SpringBootApplication
public class MsSpotiApiApplication {


    public static void main(String[] args) {
        SpringApplication.run(MsSpotiApiApplication.class, args);
    }


}
