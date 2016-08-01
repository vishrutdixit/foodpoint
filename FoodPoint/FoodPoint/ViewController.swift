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

    
    
    @IBOutlet weak var locationA: UITextField!
    
    @IBOutlet weak var locationB: UITextField!
    
    
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        let userLocation = CLLocationManager()
        
        guard let testLatitude = userLocation.location?.coordinate.latitude else {
            return
        }
        
        guard let testLongitude = userLocation.location?.coordinate.longitude else {
            return
        }
        
        print(testLatitude)
        print(testLongitude)
        
        
        let mapView = MGLMapView(frame: view.bounds)
        
        mapView.setCenterCoordinate(CLLocationCoordinate2D(latitude: testLatitude, longitude: testLongitude), zoomLevel: 12, animated: false)
        
        view.addSubview(mapView)
        
        let point = MGLPointAnnotation()
        point.coordinate = CLLocationCoordinate2D(latitude: testLatitude, longitude: testLongitude)
        point.title = "Your Location"
        
        mapView.addAnnotation(point)
        
        
        
        
        
        
        
        
        
        
        
    }
    func mapView(mapView: MGLMapView, annotationCanShowCallout annotation: MGLAnnotation) -> Bool {
        // Always try to show a callout when an annotation is tapped.
        return true
    }
    

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
        
        
        
    }


}

