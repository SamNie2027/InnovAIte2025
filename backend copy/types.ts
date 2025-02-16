import { Request } from 'express';

export interface PictureRequest extends Request {
    body: {
      picture: string,
      longitude: number,
      latitude: number,
    };
  }