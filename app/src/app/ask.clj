(ns app.ask
  (:require [clj-http.client :as client]))

(def youdao-key-from "api key from"
  "learn-english-cfw")

  (def youdao-api-key "youdao-api-key"
    "711979406")

(def youdao-api "dict api"
  (str
   "http://fanyi.youdao.com/openapi.do?keyfrom="
   youdao-key-from
   "&key="
   youdao-api-key
   "&type=data&doctype=json&version=1.1&q="))

(defn ask-youdao
  [word]
  (client/get (str youdao-api word)))

(ask-youdao "apple")


