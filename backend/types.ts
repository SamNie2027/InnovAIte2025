import { Request } from 'express';

export interface PictureRequest extends Request {
    body: {
      picture: string,
      latitude: number,
      longitude: number,
    };
  }