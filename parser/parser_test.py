'''
;; Testing read of numbers
1
;=>1
7
;=>7
  7   
;=>7
-123
;=>-123


;; Testing read of symbols
+
;=>+
abc
;=>abc
   abc   
;=>abc
abc5
;=>abc5
abc-def
;=>abc-def


;; Testing read of lists
(+ 1 2)
;=>(+ 1 2)
()
;=>()
(nil)
;=>(nil)
((3 4))
;=>((3 4))
(+ 1 (+ 2 3))
;=>(+ 1 (+ 2 3))
  ( +   1   (+   2 3   )   )  
;=>(+ 1 (+ 2 3))
(* 1 2)
;=>(* 1 2)
(** 1 2)
;=>(** 1 2)
(* -3 6)
;=>(* -3 6)

;; Test commas as whitespace
(1 2, 3,,,,),,
;=>(1 2 3)
'''
import parser

parser.parser_instance.parse('2')