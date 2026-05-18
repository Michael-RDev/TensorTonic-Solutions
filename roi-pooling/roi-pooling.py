def roi_pool(feature_map, rois, output_size):
    """
    Apply ROI Pooling to extract fixed-size feature maps from regions of interest.
    
    Args:
        feature_map (List[List[int]]): 2D grid representing the input feature map.
        rois (List[List[int]]): List of ROIs, where each ROI is defined as [x1, y1, x2, y2].
        output_size (int): The target height and width of the pooled output grid.
        
    Returns:
        List[List[List[int]]]: A list of 2D grids of size output_size x output_size, 
                               one for each input ROI.
    """
    H = len(feature_map)
    W = len(feature_map[0]) if H > 0 else 0
    pooled_outputs = []
    
    for roi in rois:
        x1, y1, x2, y2 = roi
        roi_h = y2 - y1
        roi_w = x2 - x1
        
        roi_pooled = []
        for i in range(output_size):
            row_pooled = []
            
            # Compute height boundaries for the current bin row
            hstart = y1 + (i * roi_h) // output_size
            hend = y1 + ((i + 1) * roi_h) // output_size
            if hend == hstart:
                hend = hstart + 1
                
            for j in range(output_size):
                # Compute width boundaries for the current bin column
                wstart = x1 + (j * roi_w) // output_size
                wend = x1 + ((j + 1) * roi_w) // output_size
                if wend == wstart:
                    wend = wstart + 1
                
                # Perform max pooling within the computed sub-window/bin
                max_val = None
                for r in range(hstart, hend):
                    for c in range(wstart, wend):
                        # Safeguard bounds to remain within the feature map boundaries
                        curr_r = min(max(r, 0), H - 1)
                        curr_c = min(max(c, 0), W - 1)
                        val = feature_map[curr_r][curr_c]
                        
                        if max_val is None or val > max_val:
                            max_val = val
                            
                row_pooled.append(max_val)
            roi_pooled.append(row_pooled)
            
        pooled_outputs.append(roi_pooled)
        
    return pooled_outputs