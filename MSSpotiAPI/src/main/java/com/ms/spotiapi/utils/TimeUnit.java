package com.ms.spotiapi.utils;

public enum TimeUnit {
        NANO(1), MILLI(1000000);
        private final int factor;

        TimeUnit(int factor) {
            this.factor = factor;
        }

        public long convertFromNano(long timeInNano) {
            return timeInNano / factor;
        }
}
