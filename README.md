# Overview

A simple python script for creating kubectl alias

Example of the config file

```
{
    "command": {
        "use": [ "config", "use-context" ],
        "ctx": [ "config", "current-context" ],
    },
    "object": {
        "de": "deployment"
    }
}
```

- command replaces the first argument
- object replaces the second argument if the first argument is get/edit/delete/explain

Next put the following in your `.bash_profile`

```
function _kubectl() {
    REPLACE=$(kube-parse-args.py $*)
    kubectl ${REPLACE}
}


if [ -n "$(which kubectl)" ]; then
    if [ -n "$(which kube-parse-args.py)" ]; then
        alias k=_kubectl
    else
        alias k=kubectl
    fi
fi
```

Now you should be able to run

`k ctx` which will run `kubectl config current-context`

or

`k get de` which will then run `kubectl get deployment`
