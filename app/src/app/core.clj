(ns app.core
  (:gen-class)
  (:use [io.aviso.ansi]
        [io.aviso.logging]))

(install-pretty-logging)

(def cli-prompt "➜")

(def should-exit? false)

(def token-file "~/.shanbay_token")

(def exit-command ["exit" "q" "quit"])

(def app-ascii "•?((¯°·._.• ȼℓ๏jµя€ $hąɲβą¥ •._.·°¯))؟•")

(defn log-info []
  (println (str (bold (green app-ascii)))))

(defn print-prompt []
  (print (str (bold (green cli-prompt)))))




(defn command-control
  "control the command"
  []
  (let [input (read-line)]
    (print input)))

(defn -main 
  "main"
  [& args]
  (log-info)
  (print-prompt)
  (loop [input (command-control)]
    (if-not (some #(= input %) exit-command)
      (do (print-prompt)
          (recur (command-control)))
      (do (println (str (bold (green "EXIT"))))))))
