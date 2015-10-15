(ns app.core
  (:gen-class))

(defn foo
  "I don't do a whole lot."
  [x]
  (println x "Hello, World!"))

(defn -main 
  "main"
  [& args]  
  (println args "hello world!"))




