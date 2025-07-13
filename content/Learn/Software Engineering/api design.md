---
title: api design
created: 2025-07-12
updated: 2025-07-12

---

# udemy course on rest api
https://www.udemy.com/course/rest-api/
## prerequisite
- node
- mongodb
- 

## parts
- fundamental of api * api value chain
- rest api design principles and practices
- rest api implementation patterns
- rest api security
- building the api * swagger specifications
- api management

tips
- contextualise to org
- relate to pattern to use case
- go through api for example org

# api case study:
acme
    external services--> api management --> api --> backend 

rest api framework (node.js)
    express
    hapi
     restify
     strongloop (IBM)

api management platform
    ibm api connect
    mulesoft
    apigee
    
    akana 
    mashery
    wso2
    3scale

    mongo db atlas/cloud


evolution of rpc and rest json
     
    api is an rpc mechanism

    rest is api that follows rest design principles

    rest
        representational state transfer
        6 principles
            uniform interface
                individual resources are identified in requests uri /url
                representation of resources
                self descriptive messages - metadata
                hypermedia
                crud
            stateless
                client manage its own state
                requests are self contained
            client server
                decouple
                    no impact of change
                    independent evolution
                    separation of concerns
            cacheable
                http header to control the cache behaviour
                managing it's own state 
                    lead to increase chattiness (multiple calls to get resources) because client need to send state data to server

                cache control directives (part of http header)
                cache-control
                    can have multiple
                    no-store, private, public, max-age
                expires
                last modified
                etag
                application (cache) <- api gateway/proxy (cache) <- api server (cache) <- database (read cache)
            layer system
                client > gateway > load balancer > rest api > database
                one layer only communicate with another
                no bypass
            code on demand
                hateoas
                    hypertext as the engine of application state
                    in response returned by server, also included subsequent potential action allowed to be done on the resource (aka subsequent rest api links)
                    server knows the resource state - leads to efficiencies
                    server may chagne the uri without breaking the client
                    server may add new functionality


    1991 corba
    1998 soap

    webservice = rpc over internet
    http xml
    http soap/xml
    http json
    http rest

    why rest
        common set of design principals
        best practices for building and managing rest api
        compatible with any data format
        simplicity | flexibility

    rest is not tied to protocal, i.e. could be http

    what makes api restful
        set of principles
        architectural
        api exposes resources
    not tied to tech, standard, http/json

types of api

    private 
        used by dev team internal

    public or external
        use from website/app

    partner
        trusted org

    no diff in implementation
    but in management

    considerations
        api security 
            token vs oauth secret
        access request
            email ticket vs portal
        documentiaton
            pdf vs webpage
        sla management
            monitor throughput and uptime tier for different types

api value chain
    direct revenue (subscription)
    indirect benefit (ebay, fedex, indeed)
        partner eco system 
        agility
        brand recognition
        competitive advantage 
        social good
    end consumer of asset:
        individual users
            .
        enterprise users
            .
    asset -> api dev -> api -> app dev --> app -> end user


    RMM

        level 0 (not rest)    
            rpc, plain old xml (pox)
            http get & post
            soap
            typically dont use put or delete
        LEVEL 1 
            resources + uri
            
            pov collection of resources rather than endpoint or urls

            e.g. vacation reviews photograph
        level 2 
            resources + uri + http verbs
            verbs:
                get post delete put
            crud
                create post
                retrieve get
                update put
                delete delete
        level 3 
            hypermedia
            hateoas


        https://stackoverflow.com/questions/30967822/when-do-i-use-path-parameters-vs-query-parameters-in-a-restful-api

    web app vs rest api
        both use 
            client server
            layered
            caching
            code on demand (hateoas)
        uniform interface
            webapp
                no hard & fast rules
            rest
                strict rules & best practices
                contract resource identity
        statelessness
            webapp
                depend on the need
            rest
                server never manage application state
        http
            webapp 
                get post
            rest 
                crud