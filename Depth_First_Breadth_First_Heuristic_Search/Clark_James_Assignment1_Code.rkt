#lang racket




;--------------------------------------------------
;------------------ Depth First Search ------------
;--------------------------------------------------


(define listOfWords (list "add" "ado" "age" "ago" "aid" "ail" "aim"
                          "air" "and" "any" "ape" "apt" "arc" "are"
                          "ark" "arm" "art" "ash" "ask" "auk" "awe" "awl"
                          "aye" "bad" "bag" "ban" "bat" "bee" "boa" "ear"
                          "eel" "eft" "far" "fat" "fit" "lee" "oaf" "rat" "tar"
                          "tie"))

(define (listToString myList)
  (apply string-append myList))

(define (getH1 yo)
  (listToString (list (string (string-ref (car yo) 0))(string (string-ref (cadr yo) 0)) (string (string-ref (caddr yo) 0)))))
(define (getH2 yo)
  (listToString (list (string (string-ref (car yo) 1))(string (string-ref (cadr yo) 1)) (string (string-ref (caddr yo) 1)))))
(define (getH3 yo)
  (listToString (list (string (string-ref (car yo) 2))(string (string-ref (cadr yo) 2)) (string (string-ref (caddr yo) 2)))))


(define (push el stack)
  (cons el stack))

(define (fixStack stack newStack)
  (cond
    ((null? stack)
     (car (list newStack)))
    ((< 0 (length stack))
     (fixStack (cdr stack)(push (flatten (car stack)) newStack)))))

(define (writeStuff horizontal vertical)
  (println "Goal Found ")
  (write "Horizontal ")
  (println  horizontal)
  (write  "Vertical ")
  (println vertical)
  #t)


(define (checkForGoal stack)
  (cond
    ((null? stack)
     #f)
    ((< 0 (length stack))
        (if (and
        (if (member (caddr (list (getH1 (car stack)) (getH2 (car stack))(getH3 (car stack)))) listOfWords)#t #f)
             (and (if (member (car (list (getH1 (car stack)) (getH2 (car stack))(getH3 (car stack)))) listOfWords)#t #f)
                  (if (member (cadr (list (getH1 (car stack)) (getH2 (car stack))(getH3 (car stack)))) listOfWords) #t #f)))
         (writeStuff (car stack) (list (getH1 (car stack)) (getH2 (car stack))(getH3 (car stack))))
            
          (checkForGoal (cdr stack))
          )
      )
    )
  )

(define (thirdLevelDepthFirst stack listPassed thirdStack)
  (cond
    ((null? stack)
     (if (checkForGoal (fixStack thirdStack (list))
        ) (write "Goal Found") (write "No Goal Found Today")))
    ((null? listPassed)
    (if (checkForGoal (fixStack thirdStack (list)))
        (write  " :)" )
       (thirdLevelDepthFirst (cdr stack) listOfWords (list))))
    ((< 0 (length stack))
       (thirdLevelDepthFirst  stack (cdr listPassed) (push (push (car stack)(car listPassed)) thirdStack)))))


(define (secondLevelDepthFirst stack listPassed secondStack)
  (cond
    ((null? stack)
     (thirdLevelDepthFirst secondStack listOfWords (list)))
    ((null? listPassed)
       (secondLevelDepthFirst (cdr stack) listOfWords secondStack))
    ((< 0 (length stack))
       (secondLevelDepthFirst  stack (cdr listPassed) (push (push (car stack)(car listPassed)) secondStack)))))


(define (firstLevelDepthFirst stack listPassed)
  (cond
    ((null? listPassed)
       (secondLevelDepthFirst stack listOfWords (list)))
    ((< 0 (length listPassed))
     (firstLevelDepthFirst (push (car listPassed) stack) (cdr listPassed))))
  )




;----------------------------------------------------
;---------- Breadth First Search --------------------
;----------------------------------------------------


(define (enque el queue)
   (append queue (list el)))

(define (enque2 el queue)
  (cons  queue(list el)))



(define (fixqueue queue newqueue)
  (cond
    ((null? queue)
     (car (list newqueue)))
    ((< 0 (length queue))
     (fixqueue (cdr queue)(enque (flatten (car queue)) newqueue)))))

(define (checkForGoalBreadthFirst queue)
  (cond
    ((null? queue)
     (write "No Goal Found :( "))
    ((< 0 (length queue))
        (if (and
        (if (member (caddr (list (getH1 (car queue)) (getH2 (car queue))(getH3 (car queue)))) listOfWords)#t #f)
             (and (if (member (car (list (getH1 (car queue)) (getH2 (car queue))(getH3 (car queue)))) listOfWords)#t #f)
                  (if (member (cadr (list (getH1 (car queue)) (getH2 (car queue))(getH3 (car queue)))) listOfWords) #t #f)))
          (writeStuff (car queue) (list (getH1 (car queue)) (getH2 (car queue))(getH3 (car queue))))
          (checkForGoalBreadthFirst (cdr queue))
          )
      )
    )
  )

(define (thirdLevelBreadthFirst queue listPassed thirdqueue)
  (cond
    ((null? queue)
     (checkForGoal (append queue (fixqueue thirdqueue (list)))))
    ((null? listPassed)
       (thirdLevelBreadthFirst (cdr queue) listOfWords thirdqueue))
    ((< 0 (length queue))
       (thirdLevelBreadthFirst  queue (cdr listPassed) (enque (enque2 (car queue)(car listPassed)) thirdqueue)))))


(define (secondLevelBreadthFirst queue listPassed secondqueue)
  (cond
    ((null? queue)
     (thirdLevelBreadthFirst secondqueue listOfWords (list)))
     
    ((null? listPassed)
       (secondLevelBreadthFirst (cdr queue) listOfWords secondqueue))
    ((< 0 (length queue))
       (secondLevelBreadthFirst  queue (cdr listPassed) (enque (enque2 (car queue)(car listPassed)) secondqueue)))))


(define (firstLevelBreadthFirst queue listPassed)
  (cond
    ((null? listPassed)
       (secondLevelBreadthFirst queue listOfWords (list)))
    ((< 0 (length listPassed))
     (firstLevelBreadthFirst (enque (car listPassed) queue) (cdr listPassed))))
  )



;-----------------------------------------
;------------ Heuristic Search/ Best First-
;------------------------------------------


(define vowels (list "a" "e" "i" "o" "u"))


(define (countVowel words)
(+ ( + (if (member (string (string-ref (car words) 0)) vowels) 1 0)
     (+ (if (member (string (string-ref (car words) 1)) vowels) 1 0)
          (if (member (string (string-ref (car words) 2)) vowels) 1 0)))
  ( + (if (member (string (string-ref (cdr words) 0)) vowels) 1 0)
     (+ (if (member (string (string-ref (cdr words) 1)) vowels) 1 0)
          (if (member (string (string-ref (cdr words) 2)) vowels) 1 0)))))
  

(define (heuristic stack list1 list2 list3 list4)
  (cond 
	((null? stack)
		(append list4 (append list3 (append list2 list1))))
	((= 4 (countVowel (car stack)))
                (heuristic (cdr stack) list1 list2 list3 (push (car stack) list4 )))
        ((= 3 (countVowel (car stack)))
		(heuristic (cdr stack) list1 list2 (push (car stack) list3) list4 ))
        ((= 2 (countVowel (car stack)))
		(heuristic (cdr stack) list1 (push (car stack) list2 ) list3 list4))
        ((= 1 (countVowel (car stack)))
		(heuristic (cdr stack) (push (car stack) list1 ) list2 list3 list4))))



(define (thirdLevelHeuristic stack listPassed thirdStack)
  (cond
    ((null? stack)
     (if (checkForGoal (fixStack thirdStack (list))
        ) (write "Goal Found") (write "nope")))
    ((null? listPassed)
    (if (checkForGoal (fixStack thirdStack (list)))
        (write  " :)" )
       (thirdLevelHeuristic (cdr stack) listOfWords (list))))
    ((< 0 (length stack))
       (thirdLevelHeuristic  stack (cdr listPassed) (push (push (car stack)(car listPassed)) thirdStack)))))



(define (secondLevelHeuristic stack listPassed secondStack)
  (cond
    ((null? stack)
    (thirdLevelHeuristic (heuristic secondStack (list) (list) (list) (list)) listOfWords (list)))
    ((null? listPassed)
       (secondLevelHeuristic (cdr stack) listOfWords secondStack))
    ((< 0 (length stack))
       (secondLevelHeuristic  stack (cdr listPassed) (push (push (car stack)(car listPassed)) secondStack)))))


(define (firstLevelHeuristic stack listPassed)
  (cond
    ((null? listPassed)
       (secondLevelHeuristic stack listOfWords (list)))
    ((< 0 (length listPassed))
     (firstLevelHeuristic (push (car listPassed) stack) (cdr listPassed))))
  )


;UNCOMMENT TO RUN DEPTH FIRST SEARCH
(println "BEGIN DEPTH FIRST SEARCH")
(firstLevelDepthFirst (list) listOfWords)

;UnComment to Run Breadth First Search
;FYI Breadth First Takes a While
;(println "Begin BreadthFirst Search")
;(firstLevelBreadthFirst (list) listOfWords)

;Uncomment to run the Heuristic Search
;(println "Begin Heuristic/ Best Fit Search")
;(firstLevelHeuristic (list) listOfWords)