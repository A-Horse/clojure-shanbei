(defproject app "0.1.0"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.7.0"]
                 [acyclic/squiggly-clojure "0.1.4"]
                 [org.xerial/sqlite-jdbc "3.7.2"]
                 [yesql "0.5.1"]
                 [clj-http "2.0.0"]
                 [io.aviso/pretty "0.1.19"]
                 [org.clojure/tools.logging "0.3.1"]]
  :plugins [[lein-environ "1.0.0"]]
  :profiles {:dev {:env {:squiggly {:checkers [:eastwood]
                                    :eastwood-exclude-linters [:unlimited-use]}}}}
  :env {:squiggly {:checkers [:eastwood]
                   :eastwood-exclude-linters [:unlimited-use]}}
  :main app.core
  :aot [app.core]
  :jvm-opts ^:replace []
  :uberjar {:aot :all})
