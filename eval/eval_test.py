'''
;; Testing evaluation of arithmetic operations

;; -------- Deferrable/Optional Functionality --------

;; Testing evaluation within collection literals
[1 2 (+ 1 2)]
;=>[1 2 3]

{"a" (+ 7 8)}
;=>{"a" 15}

{:a (+ 7 8)}
;=>{:a 15}

'''
import eval


def run_test():
    print("Running eval_test.py")

    result = eval.evaluate("1")
    assert result == 1

    result = eval.evaluate("(+ 5 (* 2 3))")
    assert result == 11

    result = eval.evaluate("(- (+ 5 (* 2 3)) 3)")
    assert result == 8

    result = eval.evaluate("(/ (- (+ 5 (* 2 3)) 3) 4)")
    assert result == 2

    result = eval.evaluate("(/ (- (+ 515 (* 87 311)) 302) 27)")
    assert result == 1010

    result = eval.evaluate("(* -3 6)")
    assert result == -18

    result = eval.evaluate("(/ (- (+ 515 (* -87 311)) 296) 27)")
    assert result == -994

    result = eval.evaluate("(abc 1 2 3)")
    assert result == ".*\'abc\' not found.*" #Need to write some error handling here

    result = eval.evaluate("()")
    assert result == '()'#Should this be some special kind of data?

    result = eval.evaluate("(+ 1 2)")
    assert result == 3

    print("Eval_test.py -- Done!")



if __name__ == '__main__':
    run_test()