(ns app.core
  (:gen-class)
  (:use [io.aviso.ansi]))

(def cli-prompt "> "
  "cli prompt")

(def should-exit? false)

(def token-file "~/.shanbay_token")

(def exit-command ["exit" "e"])

(defn -main 
  "main"
  [& args]
  ;;(println (str (bold (green "➜"))))
  (loop [input (read-line)]
    (if-not (some #(= input %) (list exit-command))
      (println input)
      (recur (read-line)))))
