(ns app.db
  (:require [clojure.java.jdbc :refer :all]
            [yesql.core :refer [defqueries]]))


(def db-spec {:classname "org.sqlite.JDBC"
              :subprotocol "sqlite"
              :subname "~/.learn-english.db"})







