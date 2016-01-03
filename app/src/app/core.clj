(ns app.core
  (:gen-class)
  (:use [io.aviso.ansi]
        [io.aviso.logging]))

(install-pretty-logging)

(def cli-prompt "➜")

(def should-exit? false)

(def exit-command ["exit" "q" "quit"])

(def app-ascii "•?((¯°·._.• ȼℓ๏jµя€ $hąɲβą¥ •._.·°¯))؟•")

(defn log-info []
  (println (str (bold (green app-ascii)))))

(defn print-prompt []
  (println (str (bold (green cli-prompt)))))

(defn -main 
  "main"
  [& args]
  (log-info)
  (loop [input (read-line)]
    (if-not (some #(= input %) exit-command)
      (do (println input)
          (recur (read-line)))
      ;;exit
      (println (str (bold (green "EXIT")))))))



(defn command-control
  "control the command"
  [command &rset]
  
  )
