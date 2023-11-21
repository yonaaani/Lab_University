(deffacts employees
   (employee Ivanov 7 3 5000)
   (employee Petrov 10 1 6000)
   (employee Sidorov 3 2 4500)
   (employee Kozlov 15 0 7000)
   (employee Popov 8 4 5500)
)

(defrule rule1
   (employee ?lastname ?experience ?children ?salary)
   (or (>= ?experience 5) (>= ?children 2))
   =>
   (assert (bonus ?lastname (* 0.2 ?salary)))
)

(defrule rule2
   (not (exists (employee ?lastname ?experience ?children ?salary)))
   =>
   (printout t "All employees have received a bonus." crlf)
)

(defrule rule3
   (employee ?lastname ?experience ?children ?salary)
   (>= ?experience 20)
   =>
   (printout t ?lastname " is a labor veteran." crlf)
)