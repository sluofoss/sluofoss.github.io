---
title: Personal Display Requirements
created: 2025-07-21T21:35
updated: 2025-07-21T21:35
---

# State
2 x 1920×1080 monitors

laptop:
2 x usb 3.1 ~ dp 1.2a
1 x hdmi 1.4b

pc:
1 x HDMI 2.1 
3 x DisplayPort 1.4a

laptop 2 

    3 x Thunderbolt 4 (USB-C) ports with support for:
        Charging
        DisplayPort
        Thunderbolt 4 (up to 40 Gbps)
        USB 4 (up to 40 Gbps)

# list of questions/problems that one need to solve to get this working
1. does mac support usb c split between either:
  - 2 dp
  - 2 hdmi
  - dp + hdmi
- if yes then
1. can the dock support mst multi stream transport
2. can the kvm suppport mst 
3. 
https://www.reddit.com/r/mac/comments/1h58a3h/why_doesnt_apple_support_mstmulti_stream_transport/


# initial idea/plan

```mermaid
flowchart LR
    subgraph laptop1[laptop 1 windows]
        usbc3.1/dp1.2a["
            usbc3.1/dp1.2a
            Intel HD Graphics 620
            supports three independent displays;
            Max resolution: 4096x2304@60Hz (USB Type-C); 4096x2160@30Hz (HDMI)
        "]
    end

    subgraph laptop2[laptop 2 mac]
        usbc4/thunderbolt/dp1.4a
    end

    subgraph pc
    end

    subgraph docking
    end

    subgraph kvm
        subgraph input1
            usba1[usba]
            hdmi/dp11[hdmi/dp]
            hdmi/dp12[hdmi/dp]

        end
        subgraph input2
            usba2[usba]
            hdmi/dp21[hdmi/dp]
            hdmi/dp22[hdmi/dp]
        end
    end

    subgraph visual
        direction TB
        monitor1[monitor 1 FHD 75 Hz]
        monitor2[monitor 1 FHD 100 Hz]
    end
    subgraph peripheral
        direction TB
        mouse[mouse - usb a]
        keyboard[keyboard - usb a]
        speaker[speaker - usb a + 3.5mm jack]
        camera[camera and mic - usb a]
        other[other usb devices] 
        style speaker stroke-dasharray: 5 5   
        style camera stroke-dasharray: 5 5    
    end

    kvm --> visual
    kvm --> peripheral

    pc --> usba2
    pc --> hdmi/dp21[hdmi/dp]
    pc --> hdmi/dp22[hdmi/dp]
    docking --peripheral--> usba1
    docking --display--> hdmi/dp11[hdmi/dp]
    docking --display--> hdmi/dp12[hdmi/dp]

    usbc3.1/dp1.2a --> docking
    usbc4/thunderbolt/dp1.4a -.-> docking
```

# information on daisy chaining
https://www.anker.com/blogs/hubs-and-docks/how-to-daisy-chain-monitors-with-displayport

1. Check that your gear supports MST

    GPU: Your laptop or graphics card must have a DisplayPort 1.2 (or newer) output that specifically lists MST support.
    Monitors: Every screen in the chain needs a DisplayPort 1.2+ input, and any monitor that comes before the last one in the chain also needs a DisplayPort output (usually labeled "DP Out") to pass the signal along. The last one can be an input-only model.

# information on Thunderbolt 4 and usb4
https://www.reddit.com/r/UsbCHardware/comments/nd9yjz/what_happens_if_you_connect_a_thunderbolt_3_dock/

1. does this work for both laptop?

    tb 4 is intel branding for usb4, hence backward compatible with usb 3.1

    
    https://www.reddit.com/r/macbookpro/comments/qopv72/comment/i0a72ue/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

    > You are indeed correct. macOS only supports Thunderbolt daisy chaining. They never bothered implementing USB-C DisplayPort MST.
     
    it seems that one mac cant use usb3 dp_alt?


# options
## option 0 simplified
- new to buy:
  - monitor1 ($500-$700) # if we consider the monitor upgrade (aka giving away the existing monitor ($80~$100)) then the cost comes down to $400 to $600 with benefit of set up simplicity.
  - dp cable x 1 
  - tb4 cable (supporting both thunderbolt 4 and dp1.2_alt from backward compatible)
```mermaid
flowchart LR
    subgraph option1_simplified
        direction LR
        0laptop1[laptop1 windows]
        0laptop2[laptop2 mac]
        %%0docking[docking]
        %%0kvm[kvm]
        0cable[[single cable]]
        0pc[pc]
        0peripherals[peripherals]
        

        0monitor1["monitor1 (new with inbuilt kvm & usn hub)"]  
        0monitor2["monitor2 (old msi)"]

        0laptop1 -."dp1.2_alt".-> 0cable
        0laptop2 --"TB4"--> 0cable
        0cable  -.dp.-> 0monitor1 --daisy_chain--> 0monitor2
        0pc --dp--> 0monitor1
        0peripherals --usb--> 0monitor1
    end
```

## option 1 simplified (delete)
- new to buy:
  - monitor1 ($500-$700)
  - dp cable x 2
  - tb4 cable
  - docking
```mermaid
flowchart LR
    subgraph option1_simplified
        direction LR
        0laptop1[laptop1 windows]
        0laptop2[laptop2 mac]
        0docking[docking]
        %%0kvm[kvm]
        0pc[pc]
        0peripherals[peripherals]
        

        0monitor1["monitor1 (new with inbuilt kvm & usn hub)"]  
        0monitor2["monitor2 (old msi)"]

        0laptop1 -."dp1.2_alt".-> 0docking
        0laptop2 --"TB4"--> 0docking
        0docking  -.dp.-> 0monitor1 --daisy_chain--> 0monitor2
        0pc --dp--> 0monitor1
        0peripherals --usb--> 0monitor1
    end
```

## option 1 (delete)
- new to buy:
  - dp x 4
  - tb4 cable
  - kvm
  - docking
```mermaid
flowchart LR
    subgraph option1
        direction LR
        1laptop1[laptop1 windows]
        1laptop2[laptop2 mac]
        1docking[docking]
        1kvm[kvm]
        1pc[pc]
        1peripherals[peripherals]

        1monitor1["monitor1 (new)"]  
        1monitor2["monitor2 (old msi)"]

        1laptop1 -."dp1.2_alt".-> 1docking
        1laptop2 --"TB4"--> 1docking
        1docking --dp--> 1kvm --dp--> 1monitor1 --daisy_chain--> 1monitor2
        1pc --dp--> 1kvm
        1peripherals --usb--> 1kvm

    end
```

## option 2
- new to buy:
  - dp cable x 3
  - hdmi cable x 2
  - tb4 cable
  - kvm ($50~200)
  - docking ($50~200)
```mermaid
flowchart LR
    subgraph option2
        direction LR
        
        2laptop1[laptop1 windows]
        2laptop2[laptop2 mac]
        2docking[docking]
        2kvm[kvm]
        2pc[pc]
        2peripherals[peripherals]

        2monitor1["monitor1 (old lenovo)"]  
        2monitor2["monitor2 (old msi)"]

        2laptop1 --"dp1.2_alt"--> 2docking
        2laptop2 --"tb4"--> 2docking
        2docking --"dp+
               hdmi"--> 2kvm
        2pc --"dp+
               hdmi"--> 2kvm
        2kvm --hdmi--> 2monitor1 
        2kvm --dp--> 2monitor2
        2peripherals --usb--> 2kvm

    end

```

# potential daisy chain monitor:
- https://www.centrecom.com.au/dell-p2425he-24-fhd-ips-100hz-usb-c-hub-monitor?gStoreCode=Auburn&gQT=2
- https://www.scorptec.com.au/product/monitors/27-33-inch/108367-u2724de
  - has thunderbolt 4 daisy chain (+) aka laptop line
  - has usb c + dp daisy chain (+) aka pc line 
- https://www.scorptec.com.au/product/monitors/23-26-inch/103482-24b1u5301h
  - has usb c dp alt daisy chain aka laptop line
  - has dp daisy chain + usb c hub daisy chain (+) aka pc line
  - speaker (+)
  - webcam (+)
- https://www.gigabyte.com/Monitor/M27UP/sp#sp
  - upstream usb c pd too low
## considered but rejected for reasons:
### philips
- https://www.usa.philips.com/c-p/40B1U6903CH_27/business-monitor-5k2k-ultrawide-thunderbolttm-monitor
- https://www.usa.philips.com/c-p/27B1U7903_27/professional-monitor-4k-uhd-mini-led-thunderbolttm-4-monitor
- https://www.usa.philips.com/c-p/27E2F7903_27/monitor-4k-uhd-monitor
  - suspect issues with daisy chaining and kvm at the same time

# usb c cable specs
- wrt charging the only thing that is relevant out of voltage, ampere, and watt is ampere (the amount of current passing through the cable)