(ns app.word.manager
  (:require [clojure.java.jdbc :refer :all]
            [yesql.core :refer [defqueries]]))


(def db-spec {:classname "org.sqlite.JDBC"
              :subprotocol "sqlite"
              :subname "/Users/soul/learn-english.db"})

(defqueries "word.sql"
  {:connection db-spec})


