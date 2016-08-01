//
//  ViewController.swift
//  FoodPoint
//
//  Created by Suraj Sinha on 7/31/16.
//  Copyright © 2016 KingSoy. All rights reserved.
//

import UIKit
import Mapbox




class ViewController: UIViewController, MGLMapViewDelegate {

    @IBOutlet var mapView: MGLMapView!
    
    
       
    
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        
        let userLocation = CLLocationManager()
        guard let testLatitude = userLocation.location?.coordinate.latitude
            else {
                return
        }
        guard let testLongitude = userLocation.location?.coordinate.longitude
            else {
                return
        }
    
        print (testLatitude)
        print (testLongitude)
        
        
        
        
    }
    

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
        
        
        
    }


}

