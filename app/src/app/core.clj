(ns app.core
  (:gen-class)
  (:use [io.aviso.ansi]
        [io.aviso.logging]))

(install-pretty-logging)

(def cli-prompt "> "
  "cli prompt")

(def should-exit? false)

(def token-file "~/.shanbay_token")

(def exit-command ["exit" "q" "quit"])



(def app-ascii "•?((¯°·._.• ȼℓ๏jµя€ $hąɲβą¥ •._.·°¯))؟•")

(defn log-info []
  (println str (bold ())))

(defn -main 
  "main"
  [& args]
  (println (str (bold (green "➜"))))
  (loop [input (read-line)]
    (if-not (some #(= input %) exit-command)
      (do (println input)
          (recur (read-line)))
      (do (println "EXIT")))))

