class Solution {
    float allExponent(int baseValue, int exponentValue) {
        float res;
        
        if (exponentValue >= 0) {
            Exponent exp = new Exponent(baseValue, exponentValue);
            res = (float) exp.positiveExponent();
        } else {
            // Calculate exponent using reciprocal of base raised to the positive exponent
            Exponent exp = new Exponent(baseValue, -exponentValue);
            res = 1.0f / (float) exp.positiveExponent();
        }
        
        return res;
    }
}

class Exponent {
    private int base;
    private int exponent;
    
    public Exponent(int base, int exponent) {
        this.base = base;
        this.exponent = exponent;
    }
    
    public double positiveExponent() {
        double result = 1.0;
        
        for (int i = 0; i < exponent; i++) {
            result *= base;
        }
        
        return result;
    }
}
